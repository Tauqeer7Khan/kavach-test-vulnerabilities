// Hardcoded credentials
const config = {
  apiKey: process.env.STRIPE_API_KEY,
  dbPassword: process.env.DB_PASSWORD,
  jwtSecret: process.env.JWT_SECRET
};

module.exports = config;
