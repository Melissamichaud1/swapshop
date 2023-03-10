import { createContext, useContext, useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
let internalToken = null;

export function getToken() {
  return internalToken;
}

export async function getTokenInternal() {
  const url = `${process.env.REACT_APP_swapshop_API_HOST}/token/`;
  try {
    const response = await fetch(url, {
      credentials: "include",
    });
    if (response.ok) {
      const data = await response.json();
      internalToken = data.access_token;
      return internalToken;
    }
  } catch (e) {}
  return false;
}

export async function getAccountId() {
  const url = `${process.env.REACT_APP_swapshop_API_HOST}/token/`;
  try {
    const response = await fetch(url, {
      credentials: "include",
    });
    if (response.ok) {
      const data = await response.json();
      const account = data.account.id;
      return account;
    }
  } catch (e) {}
  return false;
}

export const AuthContext = createContext({
  token: null,
  setToken: () => null,
});

export const AuthProvider = ({ children }) => {
  const [token, setToken] = useState(null);

  return (
    <AuthContext.Provider value={{ token, setToken }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuthContext = () => useContext(AuthContext);

export function useToken() {
  const { token, setToken } = useAuthContext();
  const navigate = useNavigate();

  useEffect(() => {
    async function fetchToken() {
      const token = await getTokenInternal();
      setToken(token);
    }
    if (!token) {
      fetchToken();
    }
  }, [setToken, token]);

  async function logout() {
    if (token) {
      const url = `${process.env.REACT_APP_swapshop_API_HOST}/token/`;
      await fetch(url, { method: "delete", credentials: "include" });
      internalToken = null;
      setToken(null);
      navigate("/login/");
    }
  }

  async function login(username, password) {
    const url = `${process.env.REACT_APP_swapshop_API_HOST}/token/`;
    const form = new FormData();
    form.append("username", username);
    form.append("password", password);
    const response = await fetch(url, {
      method: "post",
      credentials: "include",
      body: form,
    });
    if (response.ok) {
      const token = await getTokenInternal();
      setToken(token);
      return navigate("/");
    }
    return false;
  }

  async function signup(firstName, lastName, email, password) {
    const url = `${process.env.REACT_APP_swapshop_API_HOST}/swapshop/accounts`;
    const response = await fetch(url, {
      method: "post",
      body: JSON.stringify({
        first_name: firstName,
        last_name: lastName,
        email: email,
        password: password,
      }),
      headers: {
        "Content-Type": "application/json",
      },
    });
    if (response.ok) {
      await login(email, password);
      return navigate("/");
    }
    return false;
  }

  async function update(email, password, firstName, lastName) {
    const url = `${process.env.REACT_APP_swapshop_API_HOST}/swapshop/accounts/`;
    const response = await fetch(url, {
      method: "patch",
      body: JSON.stringify({
        email,
        password,
        first_name: firstName,
        last_name: lastName,
      }),
      headers: {
        "Content-Type": "application/json",
      },
    });
    if (response.ok) {
      await login(email, password);
    }
    return false;
  }

  return { token, login, logout, signup, update };
}
