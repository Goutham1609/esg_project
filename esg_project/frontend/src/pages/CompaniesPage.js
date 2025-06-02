import React, { useEffect, useState } from 'react';
import { Table, Typography, Spin, message } from 'antd';
import axios from 'axios';

const { Title } = Typography;

const CompaniesPage = () => {
  const [companies, setCompanies] = useState([]);
  const [loading, setLoading] = useState(false);

  const fetchCompanies = async () => {
    setLoading(true);
    try {
      const response = await axios.get('/api/companies/');
      setCompanies(response.data);
    } catch (error) {
      message.error('Failed to load companies');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchCompanies();
  }, []);

  const columns = [
    {
      title: 'Company Name',
      dataIndex: 'name',
      key: 'name',
    },
    {
      title: 'Sector',
      dataIndex: 'sector',
      key: 'sector',
    },
    {
      title: 'Location',
      dataIndex: 'location',
      key: 'location',
    },
  ];

  return (
    <div style={{ padding: '2rem' }}>
      <Title level={2}>Companies</Title>
      {loading ? (
        <Spin />
      ) : (
        <Table
          dataSource={companies}
          columns={columns}
          rowKey="id"
          pagination={{ pageSize: 5 }}
        />
      )}
    </div>
  );
};

export default CompaniesPage;
