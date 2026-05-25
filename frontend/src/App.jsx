import { useEffect, useState } from 'react'
import axios from 'axios'

function App() {
  const [records, setRecords] = useState([])
  const [file, setFile] = useState(null)

  const fetchRecords = async () => {
    const response = await axios.get('https://breathe-esg-tech-assignment.onrender.com/api/records/')
    setRecords(response.data)
  }

  useEffect(() => {
    fetchRecords()
  }, [])

  const updateStatus = async (id, status) => {
    await axios.put(`https://breathe-esg-tech-assignment.onrender.com/api/records/${id}/status/`, {
      status: status
    })

    fetchRecords()
  }

  const uploadFile = async () => {
    const formData = new FormData()
    formData.append('file', file)

    await axios.post('https://breathe-esg-tech-assignment.onrender.com/api/upload/', formData)

    fetchRecords()
  }

  return (
    <div style={{ padding: '20px' }}>
      <h1 style={{
  color: '#1e3a8a',
  marginBottom: '20px'
  }}>
  ESG Analyst Review Dashboard
  </h1>

      <h3>Upload ESG CSV File</h3>

      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <button onClick={uploadFile}>
        Upload CSV
      </button>

      <br />
      <br />

      <table border="1" cellPadding="10">
        <thead>
          <tr>
            <th>Source</th>
            <th>Activity</th>
            <th>Quantity</th>
            <th>Unit</th>
            <th>CO2e</th>
            <th>Status</th>
            <th>Flagged</th>
            <th>Action</th>
          </tr>
        </thead>

        <tbody>
          {records.map((record) => (
            <tr
              key={record.id}
              style={{
                backgroundColor: record.is_flagged ? '#ffcccc' : 'white'
              }}
            >
              <td>{record.source_type}</td>
              <td>{record.activity_type}</td>
              <td>{record.quantity}</td>
              <td>{record.unit}</td>
              <td>{record.co2e}</td>
              <td>{record.status}</td>
              <td>{record.is_flagged ? 'YES' : 'NO'}</td>
              <td>
                <button
  style={{
    backgroundColor: 'green',
    color: 'white',
    border: 'none',
    padding: '5px 10px',
    marginRight: '5px',
    cursor: 'pointer'
  }}
  onClick={() => updateStatus(record.id, 'APPROVED')}
>
                  Approve
                </button>

                <button
  style={{
    backgroundColor: 'red',
    color: 'white',
    border: 'none',
    padding: '5px 10px',
    cursor: 'pointer'
  }}
  onClick={() => updateStatus(record.id, 'REJECTED')}
>
                  Reject
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}

export default App