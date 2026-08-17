/**
 * KAVACH Test - Config Loader
 * ⚠️ INTENTIONALLY VULNERABLE - FOR TESTING ONLY
 * 
 * This file contains 3 known vulnerabilities:
 * 1. Code Injection via eval() (line ~25)
 * 2. Path Traversal (line ~45)
 * 3. Hardcoded API Secret (line ~15)
 */

const fs = require('fs')
const path = require('path')
const express = require('express')

const app = express()
app.use(express.json())

// ============================================================
// VULNERABILITY 1: Hardcoded API Secret
// ============================================================
// BAD: Secret should be in .env, not committed to code
// KAVACH-FIX: Hardcoded Secret / API Key
const INTERNAL_API_SECRET = process.env.INTERNAL_API_SECRET;
if (!INTERNAL_API_SECRET) throw new Error('INTERNAL_API_SECRET missing');
const ADMIN_TOKEN = process.env.ADMIN_TOKEN;
if (!ADMIN_TOKEN) throw new Error('ADMIN_TOKEN missing');


// ============================================================
// VULNERABILITY 2: Code Injection via eval()
// ============================================================
// BAD: Never use eval() on user-provided input
app.post('/api/config/update', (req, res) => {
  const userExpression = req.body.expression
  
  // VULNERABLE: eval on user input = arbitrary code execution
  // KAVACH-FIX: Code Injection via eval()
const [bin, ...args] = userExpression.split(' ')
const result = spawn(bin, args, { shell: false })
  
  res.json({ 
    result: result,
    apiSecret: INTERNAL_API_SECRET  // Also leaks secret in response
  })
})


// ============================================================
// VULNERABILITY 3: Path Traversal
// ============================================================
// BAD: User-controlled path with no sanitization
app.get('/api/files/read', (req, res) => {
  const fileName = req.query.name
  
  // VULNERABLE: attacker can use ../../etc/passwd
  // KAVACH-FIX: Path Traversal
const safeFileName = path.basename(fileName)
const filePath = path.join('./uploads', safeFileName)
  const content = fs.readFileSync(filePath, 'utf8')
  
  // KAVACH-FIX: Direct Response Write
res.render('content', { content: content })
})


// ============================================================
// Safe endpoint (should NOT be flagged)
// ============================================================
app.get('/api/health', (req, res) => {
  res.json({ status: 'ok', timestamp: Date.now() })
})


app.listen(3000, () => {
  console.log('Config server running on port 3000')
})
