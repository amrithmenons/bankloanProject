
import React, { useState } from 'react';
import { Container, Typography, Button, Box, TextField, MenuItem } from '@mui/material';
import './BasicInfoAccount.css';

const BasicInfoAccountPresent = () => {
  const [formData, setFormData] = useState({
    accountNumber: '',
    loanAmount: '',
    loanRequestedFor: ''
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await fetch('http://localhost:5000/basicInfoAccount', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });
      alert('Loan request sent successfully!');
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div className="apply-now-page">
      <div className="apply-now-sidebar">
        <div className="apply-now-sidebar-header">
          <img src="/path/to/logo.png" alt="Agriculture Loans" className="apply-now-logo" />
          <Typography variant="h6">कृषि ऋण</Typography>
          <Typography variant="subtitle1">Agriculture Loans</Typography>
        </div>
        <div className="apply-now-sidebar-content-basicinfo">
          <Typography variant="h6">प्रारंभिक विवरण</Typography>
          <Typography variant="subtitle1">Preliminary Details</Typography>
        </div>
      </div>
      <div className="apply-now-main-content">
        <Container>
          <Typography variant="h4" gutterBottom>कृषि ऋण | Agriculture Loan</Typography>
          <Container className="apply-now-account-details">
            <div className="apply-now-account-details-container">
              <Typography variant="h6" gutterBottom>बैंक ऑफ बड़ौदा खाते का विवरण | Bank of AMJ account Details</Typography>
              <form onSubmit={handleSubmit}>
                <TextField
                  fullWidth
                  name="accountNumber"
                  label="खाता संख्या | Account Number"
                  margin="normal"
                  variant="outlined"
                  required
                  onChange={handleChange}
                />
                <TextField
                  fullWidth
                  name="loanAmount"
                  label="आवश्यक ऋण राशि | The Loan Amount Required"
                  margin="normal"
                  variant="outlined"
                  required
                  onChange={handleChange}
                />
                <TextField
                  fullWidth
                  name="loanRequestedFor"
                  select
                  label="ऋण का अनुरोध किया गया | Loan Requested For"
                  margin="normal"
                  variant="outlined"
                  required
                  onChange={handleChange}
                >
                  <MenuItem value="Financing Agriclinics & Agribusiness">Financing Agriclinics & Agribusiness</MenuItem>
                  <MenuItem value="Advances to Food Agro Based Units">Advances to Food Agro Based Units</MenuItem>
                  <MenuItem value="Animal Husbandry and Fisheries Kisan Credit Card Scheme">Animal Husbandry and Fisheries Kisan Credit Card Scheme</MenuItem>
                  <MenuItem value="Kisan Credit Card (KCC)">Kisan Credit Card (KCC)</MenuItem>
                  <MenuItem value="Kisan Tatkal Loan Scheme">Kisan Tatkal Loan Scheme</MenuItem>
                  <MenuItem value="Financing Agencies Providing Custom Services To Farmers">Financing Agencies Providing Custom Services To Farmers</MenuItem>
                  <MenuItem value="Financing Development of Dairy, Poultry, Fishery, etc.">Financing Development of Dairy, Poultry, Fishery, etc.</MenuItem>
                  <MenuItem value="Financing Tractors and Heavy Agriculture Machinery">Financing Tractors and Heavy Agriculture Machinery</MenuItem>
                  <MenuItem value="Scheme for Purchase of Agriculture Land">Scheme for Purchase of Agriculture Land</MenuItem>
                </TextField>
                <Box mt={2}>
                  <Button type="submit" variant="contained" color="primary" fullWidth className="apply-now-submit-button">
                    प्रस्तुत करें | SUBMIT
                  </Button>
                </Box>
              </form>
            </div>
          </Container>
        </Container>
      </div>
      <div className="apply-now-right-sidebar">
        <img src="/path/to/bank-logo.png" alt="Bank of Baroda" className="apply-now-bank-logo" />
        <ul className="apply-now-sidebar-list">
          <li className="apply-now-sidebar-item">Agri Loan Features</li>
          <li className="apply-now-sidebar-item">Loan Eligibility Calculator</li>
          <li className="apply-now-sidebar-item">EMI Calculator</li>
          <li className="apply-now-sidebar-item">FAQs</li>
          <li className="apply-now-sidebar-item">User Guide Video</li>
          <li className="apply-now-sidebar-item">Toll Free No. 18002581111</li>
        </ul>
      </div>
    </div>
  );
};

export default BasicInfoAccountPresent;

