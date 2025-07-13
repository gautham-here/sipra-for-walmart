import React, { useState } from "react";

function LoginPage() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleLogin = () => {
    if (!email || !password) {
      setError("Please fill in both fields.");
    } else {
      setError("");
      alert(`Logged in as: ${email}`);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-[#65c5f5]">
      <div className="bg-white p-8 rounded-xl shadow-xl w-full max-w-md">
        <h2 className="text-[#0053e2] text-3xl font-bold text-center mb-6">
          Walmart Staff Login
        </h2>

        {error && (
          <p className="text-red-600 text-sm text-center mb-4">{error}</p>
        )}

        <input
          type="email"
          placeholder="Email"
          className="w-full px-4 py-3 border border-gray-300 rounded-md mb-4 focus:outline-none focus:ring-2 focus:ring-[#0053e2]"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />

        <input
          type="password"
          placeholder="Password"
          className="w-full px-4 py-3 border border-gray-300 rounded-md mb-6 focus:outline-none focus:ring-2 focus:ring-[#0053e2]"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />

        <button
          onClick={handleLogin}
          className="w-full bg-[#0053e2] text-white font-semibold py-3 rounded-md hover:bg-[#003cb3] transition duration-200"
        >
          Login
        </button>
      </div>
    </div>
  );
}

export default LoginPage;