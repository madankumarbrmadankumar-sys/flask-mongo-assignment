<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Submit Details</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: Arial, sans-serif; background: #f0f4f8; display: flex;
           justify-content: center; align-items: center; min-height: 100vh; }
    .card { background: white; border-radius: 10px; padding: 40px;
            width: 420px; box-shadow: 0 4px 20px rgba(0,0,0,0.1); }
    h2 { color: #1F4E79; margin-bottom: 24px; text-align: center; }
    label { display: block; margin-bottom: 6px; font-weight: bold; color: #333; font-size: 14px; }
    input, select { width: 100%; padding: 10px 14px; border: 1px solid #ccc;
                    border-radius: 6px; font-size: 14px; margin-bottom: 18px; }
    button { width: 100%; padding: 12px; background: #2E75B6; color: white;
             border: none; border-radius: 6px; font-size: 16px; cursor: pointer; }
    button:hover { background: #1F4E79; }
    .error { background: #fde8e8; border: 1px solid #e74c3c; color: #c0392b;
             padding: 12px; border-radius: 6px; margin-bottom: 18px; font-size: 14px; }
  </style>
</head>
<body>
  <div class="card">
    <h2>&#128196; Submit Your Details</h2>
    {% if error %}
      <div class="error">&#9888; {{ error }}</div>
    {% endif %}
    <form action="/submit" method="POST">
      <label for="name">Full Name</label>
      <input type="text" id="name" name="name" placeholder="Enter your name" required>
      <label for="email">Email Address</label>
      <input type="email" id="email" name="email" placeholder="Enter your email" required>
      <label for="role">Role</label>
      <select id="role" name="role" required>
        <option value="">-- Select Role --</option>
        <option value="DevOps Engineer">DevOps Engineer</option>
        <option value="Cloud Architect">Cloud Architect</option>
        <option value="SRE">SRE</option>
        <option value="Security Engineer">Security Engineer</option>
      </select>
      <button type="submit">Submit</button>
    </form>
  </div>
</body>
</html>
