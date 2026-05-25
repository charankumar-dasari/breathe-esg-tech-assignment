import pandas as pd

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import EmissionRecord, AuditLog
from .serializers import EmissionRecordSerializer


@api_view(['POST'])
def upload_csv(request):

    file = request.FILES['file']

    df = pd.read_csv(file)

    for _, row in df.iterrows():

        quantity = float(row['quantity'])

        flagged = False

        if quantity > 10000:
            flagged = True

        EmissionRecord.objects.create(
            source_type=row['source_type'],
            activity_type=row['activity_type'],
            quantity=quantity,
            unit=row['unit'],
            co2e=quantity * 2,
            is_flagged=flagged
        )

    return Response({"message": "Uploaded Successfully"})


@api_view(['GET'])
def get_records(request):

    records = EmissionRecord.objects.all()

    serializer = EmissionRecordSerializer(records, many=True)

    return Response(serializer.data)

@api_view(['PUT'])
def update_status(request, id):

    record = EmissionRecord.objects.get(id=id)

    old_status = record.status

    new_status = request.data.get('status')

    record.status = new_status
    record.save()

    AuditLog.objects.create(
        record=record,
        action='STATUS UPDATED',
        old_status=old_status,
        new_status=new_status,
        changed_by='analyst'
    )

    return Response({"message": "Status updated successfully"})