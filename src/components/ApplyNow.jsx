import React from 'react';
import { Container, Typography, Button, Box } from '@mui/material';
import './ApplyNow.css'
import { NavLink } from 'react-router-dom';
const ApplyNow = () => {
  return (
      <div className="apply-now-page">
        <div className="sidebar">
          <div className="sidebar-header">
            <img src="/path/to/logo.png" alt="Agriculture Loans" />
            <Typography variant="h6">कृषि ऋण</Typography>
            <Typography variant="subtitle1">Agriculture Loans</Typography>
          </div>
          <div className="sidebar-content">
            <Typography variant="h6">प्रारंभिक विवरण</Typography>
            <Typography variant="subtitle1">Preliminary Details</Typography>
          </div>
        </div>
        <div className="main-content">
          <div className="main-contentmiddle-applynow">
          <Container>
            <Typography variant="h4" gutterBottom>कृषि ऋण | Agriculture Loan</Typography>
            <div className="customer-status">
              <Typography variant="body1">क्या आप बैंक ऑफ बड़ौदा के ग्राहक हैं? | Are You Customer of our Service?</Typography>
              <div className="status-buttons">
              <NavLink to="/basic" className="navlink-button">
                <Button variant="outlined" className="status-button">मेरे पास बॉब खाता नहीं है | I Don't Have Bank Account</Button>
              </NavLink>
              <NavLink to="/BasicInfoAccount" className="BasicInfoAccount">
                <Button variant="outlined" className="status-button">मेरे पास बॉब खाता है | I Have Bank Account</Button>
              </NavLink>
              </div>
            </div>
          </Container>
          </div>
          <div className="right-sidebar">
            <img src="/path/to/bank-logo.png" alt="Bank of Baroda" />
            <ul>
              <li>Agri Loan Features</li>
              <li>Loan Eligibility Calculator</li>
              <li>EMI Calculator</li>
              <li>FAQs</li>
              <li>User Guide Video</li>
              <li>Toll Free No. 18002581111</li>
            </ul>
          </div>
        </div>
      </div>
    );
};

export default ApplyNow;


