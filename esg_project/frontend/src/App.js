import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { Layout, Menu } from 'antd';
import 'antd/dist/reset.css';  // Ant Design styles

import HomePage from './pages/HomePage';
import CompaniesPage from './pages/CompaniesPage';
import Dashboard from './pages/Dashboard';
import LoginPage from './pages/LoginPage';

const { Header, Content, Footer } = Layout;

const App = () => {
  return (
    <Router>
      <Layout className="layout">
        <Header>
          <div className="logo" />
          <Menu theme="dark" mode="horizontal" defaultSelectedKeys={['1']}>
            <Menu.Item key="1"><a href="/">Home</a></Menu.Item>
            <Menu.Item key="2"><a href="/companies">Companies</a></Menu.Item>
            <Menu.Item key="3"><a href="/login">Login</a></Menu.Item>
          </Menu>
        </Header>
        <Content style={{ padding: '0 50px' }}>
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/companies" element={<CompaniesPage />} />
            <Route path="/dashboard" element={<Dashboard />} />
            <Route path="/login" element={<LoginPage />} />
          </Routes>
        </Content>
        <Footer style={{ textAlign: 'center' }}>
          ESG Dashboard ©2025 Created with Ant Design
        </Footer>
      </Layout>
    </Router>
  );
};

export default App;
