/*import React from 'react';
import { Container, Typography, TextField, Button, Box, Grid } from '@mui/material';
import './BasicInformationPage.css';

const BasicInformationPage = () => {
  return (
    <div className="basic-information-page">
      <div className="sidebar">
        <div className="sidebar-header">
          <Typography variant="h6">कृषि ऋण</Typography>
          <Typography variant="subtitle1">Agriculture Loans</Typography>
        </div>
        <div className="sidebar-content">
          <Typography variant="h6">आधारभूत जानकारी</Typography>
          <Typography variant="subtitle1">Basic Details</Typography>
          <Typography variant="h6">ऋण जानकारी</Typography>
          <Typography variant="subtitle1">Loan Details</Typography>
          <Typography variant="h6">submit</Typography>
        </div>
      </div>
      <div className="main-content">
        <div className="main-contentcontaininfo">
        <Container>
          <Typography variant="h4" gutterBottom>आधारभूत जानकारी | Basic Information</Typography>
          <Grid container spacing={2}>
            <Grid item xs={12} sm={6}>
              <TextField label="Applicant's Full Name" fullWidth required />
            </Grid>
            <Grid item xs={12} sm={6}>
              <TextField label="Father's/Husband's Name" fullWidth required />
            </Grid>
            <Grid item xs={12} sm={6}>
              <TextField label="Gender" fullWidth required />
            </Grid>
            <Grid item xs={12} sm={6}>
              <TextField label="Occupation Type" fullWidth required />
            </Grid>
            <Grid item xs={12} sm={6}>
              <TextField label="Gross Annual Income" fullWidth required />
            </Grid>
            <Grid item xs={12} sm={6}>
              <TextField label="KYC Document Number" fullWidth required />
            </Grid>
            <Grid item xs={12} sm={6}>
              <TextField label="Email ID" fullWidth required />
            </Grid>
            <Grid item xs={12} sm={6}>
              <TextField label="Mobile No." fullWidth required />
            </Grid>
            <Grid item xs={12} sm={6}>
              <TextField label="Permanent Address" fullWidth required />
            </Grid>
            <Grid item xs={12} sm={6}>
              <TextField label="Address Details" fullWidth required />
            </Grid>
            <Grid item xs={12} sm={6}>
              <TextField label="Communication Address" fullWidth required />
            </Grid>
            <Grid item xs={12} sm={6}>
              <TextField label="Pin Code" fullWidth required />
            </Grid>
          </Grid>
          <Box mt={4}>
            <Button variant="outlined" color="primary" className="SaveButton">SAVE AND CONTINUE LATER</Button>
            <Button variant="contained" color="primary" className='ContainedButton'>CONTINUE</Button>
          </Box>
        </Container>
        </div>
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
  );
};

export default BasicInformationPage;*/

import React, { useState } from 'react';
import { Container, Typography, TextField, Button, Box, Grid } from '@mui/material';
import './BasicInformationPage.css';

const BasicInformationPage = () => {
  const [formData, setFormData] = useState({
    fullName: '',
    fatherOrHusbandName: '',
    gender: '',
    occupation: '',
    income: '',
    kycDocumentNumber: '',
    email: '',
    mobile: '',
    permanentAddress: '',
    addressDetails: '',
    communicationAddress: '',
    pinCode: ''
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
      await fetch('http://localhost:5000/basicInformation', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });
      alert('Data saved successfully!');
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div className="basic-information-page">
      <div className="basicinformation-final">
        <div className='basicinfo'>
        <div className="basicinfoheader">
          <Typography variant="h6">कृषि ऋण</Typography>
          <Typography variant="subtitle1">Agriculture Loans</Typography>
          <Typography variant="h6">आधारभूत जानकारी</Typography>
          <Typography variant="subtitle1">Basic Details</Typography>
          <Typography variant="h6">ऋण जानकारी</Typography>
          <Typography variant="subtitle1">Loan Details</Typography>
          <Typography variant="h6">Submit</Typography>
        </div>
        </div>
      </div>
      <div className="contentinfofinalinformation">
        <div className="contentcontaininformation">
          <Container>
            <Typography variant="h4" gutterBottom>आधारभूत जानकारी | Basic Information</Typography>
            <form onSubmit={handleSubmit}>
              <Grid container spacing={2}>
                <Grid item xs={12} sm={6}>
                  <TextField name="fullName" label="Applicant's Full Name" fullWidth required onChange={handleChange} />
                </Grid>
                <Grid item xs={12} sm={6}>
                  <TextField name="fatherOrHusbandName" label="Father's/Husband's Name" fullWidth required onChange={handleChange} />
                </Grid>
                <Grid item xs={12} sm={6}>
                  <TextField name="gender" label="Gender" fullWidth required onChange={handleChange} />
                </Grid>
                <Grid item xs={12} sm={6}>
                  <TextField name="occupation" label="Occupation Type" fullWidth required onChange={handleChange} />
                </Grid>
                <Grid item xs={12} sm={6}>
                  <TextField name="income" label="Gross Annual Income" fullWidth required onChange={handleChange} />
                </Grid>
                <Grid item xs={12} sm={6}>
                  <TextField name="kycDocumentNumber" label="KYC Document Number" fullWidth required onChange={handleChange} />
                </Grid>
                <Grid item xs={12} sm={6}>
                  <TextField name="email" label="Email ID" fullWidth required onChange={handleChange} />
                </Grid>
                <Grid item xs={12} sm={6}>
                  <TextField name="mobile" label="Mobile No." fullWidth required onChange={handleChange} />
                </Grid>
                <Grid item xs={12} sm={6}>
                  <TextField name="permanentAddress" label="Permanent Address" fullWidth required onChange={handleChange} />
                </Grid>
                <Grid item xs={12} sm={6}>
                  <TextField name="addressDetails" label="Address Details" fullWidth required onChange={handleChange} />
                </Grid>
                <Grid item xs={12} sm={6}>
                  <TextField name="communicationAddress" label="Communication Address" fullWidth required onChange={handleChange} />
                </Grid>
                <Grid item xs={12} sm={6}>
                  <TextField name="pinCode" label="Pin Code" fullWidth required onChange={handleChange} />
                </Grid>
              </Grid>
              <Box mt={4}>
                <Button type="button" variant="outlined" color="primary" className="SaveButtonbasic">SAVE AND CONTINUE LATER</Button>
                <Button type="submit" variant="contained" color="primary" className="ContainedButtonbasic">CONTINUE</Button>
              </Box>
            </form>
          </Container>
        </div>
      </div>
      <div className="right-sidebarbasicinfo">
        <img src="/path/to/bank-logo.png" alt="Bank of AMJ" />
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
  );
};

export default BasicInformationPage;

