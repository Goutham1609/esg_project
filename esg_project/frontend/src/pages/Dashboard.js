import React from "react";
import { Button } from "antd";
import { useNavigate } from "react-router-dom";

const Dashboard = () => {
  const navigate = useNavigate();

  const logout = () => {
    localStorage.removeItem("access");
    localStorage.removeItem("refresh");
    navigate("/");
  };

  return (
    <div>
      <h2>Welcome to ESG Dashboard</h2>
      <Button onClick={logout}>Logout</Button>
    </div>
  );
};

export default Dashboard;
