import React from 'react';
import { Typography, Card, Button } from 'antd';
import { Link } from 'react-router-dom';

const { Title, Paragraph } = Typography;

const HomePage = () => {
  return (
    <div style={{ padding: '2rem', maxWidth: 800, margin: 'auto' }}>
      <Card bordered style={{ boxShadow: '0 4px 12px rgba(0,0,0,0.1)' }}>
        <Title level={2}>Welcome to the ESG Data Management System</Title>
        <Paragraph>
          This platform allows you to manage environmental, social, and governance (ESG) data for companies, business units, and metrics.
        </Paragraph>
        <Paragraph>
          Use the navigation bar to:
        </Paragraph>
        <ul>
          <li>View and manage companies</li>
          <li>Access metrics and their values</li>
          <li>Log in as a user with specific roles</li>
        </ul>
        <div style={{ marginTop: '1rem' }}>
          <Link to="/companies">
            <Button type="primary">View Companies</Button>
          </Link>
          <Link to="/login" style={{ marginLeft: '1rem' }}>
            <Button>Login</Button>
          </Link>
          <Link to="/dashboard" style={{ marginLeft: '1rem' }}>
            <Button>Dashboard</Button>
          </Link>
        </div>
      </Card>
    </div>
  );
};

export default HomePage;
