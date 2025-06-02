import React, { useState } from "react";
import { Form, Input, Button, message } from "antd";
import axios from "axios";
import { useNavigate } from "react-router-dom";

const LoginPage = () => {
  const navigate = useNavigate();

  const onFinish = async (values) => {
    try {
      const res = await axios.post("http://127.0.0.1:8000/api/token/", values);
      localStorage.setItem("access", res.data.access);
      localStorage.setItem("refresh", res.data.refresh);
      message.success("Login successful");
      navigate("/dashboard");
    } catch (err) {
      message.error("Login failed");
    }
  };

  return (
    <Form
      name="login"
      onFinish={onFinish}
      layout="vertical"
      style={{ maxWidth: 400, margin: "0 auto" }}
    >
      <h2>Login</h2>
      <Form.Item
        label="Username"
        name="username"
        rules={[{ required: true, message: "Please input your username!" }]}
      >
        <Input />
      </Form.Item>

      <Form.Item
        label="Password"
        name="password"
        rules={[{ required: true, message: "Please input your password!" }]}
      >
        <Input.Password />
      </Form.Item>

      <Form.Item>
        <Button type="primary" htmlType="submit" block>
          Log in
        </Button>
      </Form.Item>
    </Form>
  );
};

export default LoginPage;
