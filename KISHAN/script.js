// Simple Personal Finance Tracker using localStorage
const STORAGE_KEY = 'personal_finance_expenses'
let expenses = []

const form = document.getElementById('expense-form')
const titleInput = document.getElementById('title')
const amountInput = document.getElementById('amount')
const expensesList = document.getElementById('expenses-list')
const totalEl = document.getElementById('total')
const clearAllBtn = document.getElementById('clear-all')

function loadExpenses(){
  try{
    const raw = localStorage.getItem(STORAGE_KEY)
    expenses = raw ? JSON.parse(raw) : []
  }catch(e){
    console.error('Failed reading expenses from localStorage', e)
    expenses = []
  }
}

function saveExpenses(){
  localStorage.setItem(STORAGE_KEY, JSON.stringify(expenses))
}

function formatAmount(n){
  return Number(n).toFixed(2)
}

function renderExpenses(){
  expensesList.innerHTML = ''
  let total = 0
  if(expenses.length === 0){
    const li = document.createElement('li')
    li.textContent = 'No expenses yet.'
    li.style.opacity = '0.7'
    expensesList.appendChild(li)
  } else {
    for(const exp of expenses){
      const li = document.createElement('li')

      const meta = document.createElement('div')
      meta.className = 'expense-meta'

      const title = document.createElement('div')
      title.className = 'expense-title'
      title.textContent = exp.title

      const amount = document.createElement('div')
      amount.className = 'expense-amount'
      amount.textContent = `$${formatAmount(exp.amount)}`

      meta.appendChild(title)

      const right = document.createElement('div')
      right.style.display = 'flex'
      right.style.alignItems = 'center'
      right.style.gap = '12px'
      right.appendChild(amount)

      const del = document.createElement('button')
      del.className = 'delete-btn'
      del.textContent = 'Delete'
      del.dataset.id = exp.id
      del.addEventListener('click', () => removeExpense(exp.id))

      right.appendChild(del)

      li.appendChild(meta)
      li.appendChild(right)

      expensesList.appendChild(li)

      total += Number(exp.amount)
    }
  }

  totalEl.textContent = formatAmount(total)
}

function addExpense(title, amount){
  const expense = { id: Date.now().toString(), title: title.trim(), amount: Number(amount) }
  expenses.unshift(expense)
  saveExpenses()
  renderExpenses()
}

function removeExpense(id){
  expenses = expenses.filter(e => e.id !== id)
  saveExpenses()
  renderExpenses()
}

function clearAll(){
  if(!confirm('Clear all expenses? This cannot be undone.')) return
  expenses = []
  saveExpenses()
  renderExpenses()
}

form.addEventListener('submit', (e) => {
  e.preventDefault()
  const title = titleInput.value
  const amount = amountInput.value
  if(!title || !amount) return
  addExpense(title, amount)
  form.reset()
  titleInput.focus()
})

clearAllBtn.addEventListener('click', clearAll)

// init
loadExpenses()
renderExpenses()
