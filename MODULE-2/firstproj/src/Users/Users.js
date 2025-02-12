// import react from 'react';
// const Users = () => {
//     return <h2>User works!</h2>
// }
// export default Users;



import React from 'react';

import './Forms.css';

const Users = () => {
  const [principal, setPrincipal] = React.useState('');
  const [rate, setRate] = React.useState('');
  const [time, setTime] = React.useState('');
  const [simpleInterest, setSimpleInterest] = React.useState(null);
  const [compoundInterest, setCompoundInterest] = React.useState(null);

  const calculateInterest = () => {
    const P = parseFloat(principal);
    const R = parseFloat(rate) / 100;
    const T = parseFloat(time);

    const SI = (P * R * T).toFixed(2);
    const CI = (P * Math.pow((1 + R), T) - P).toFixed(2);

    setSimpleInterest(SI);
    setCompoundInterest(CI);
  };

  return (
    <div>
      <div className='Header'><h2>Interest Calculator</h2></div>
      <div className='form-card'>
      <form onSubmit={(e) => { e.preventDefault(); calculateInterest(); }}>
        <div className='Text_Box'>
          <label>Principal:</label>
          <input type="number" value={principal} onChange={(e) => setPrincipal(e.target.value)} required />
        </div>
        <div>
          <label>Rate of Interest (%):</label>
          <input type="number" value={rate} onChange={(e) => setRate(e.target.value)} required />
        </div>
        <div>
          <label>Time (years):</label>
          <input type="number" value={time} onChange={(e) => setTime(e.target.value)} required />
        </div>
        <button type="submit">Calculate</button>
      </form>
      </div>
      {simpleInterest !== null && (
        <div>
          <h3>Results:</h3>
          <p>Simple Interest: {simpleInterest}</p>
          <p>Compound Interest: {compoundInterest}</p>
        </div>
      )}
    </div>
  );
};

export default Users;

{/* <style>
    .Header{
        color: 'white'
    }
// </style> */}