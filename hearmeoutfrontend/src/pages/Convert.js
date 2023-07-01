import React, { useState, useEffect } from 'react';

function Convert() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch('/conversions')
      .then((res) => res.json())
      .then((data) => {
        setData(data);
        console.log(data);
      })
      .catch((error) => console.error(error));
  }, []);

  return (
    <div>
      {data.length === 0 ? (
        <p>Loading...</p>
      ) : (
        data.map((conversion) => (
          <div key={conversion.id}>
            <p style={{ color: 'white' }}>Input: {conversion.input}</p>
            <p style={{ color: 'white' }}>Output: {conversion.output}</p>
          </div>
        ))
      )}
    </div>
  );
}

export default Convert;
