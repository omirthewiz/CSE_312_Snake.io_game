// ===== GAME CLIENT (render + input) - OWNER: You (Person 4) =====
const canvas=document.getElementById('game')
const ctx=canvas.getContext('2d')
const status=document.getElementById('status')

const proto=location.protocol=='https:'?'wss://':'ws://'
const ws=new WebSocket(proto+location.host+'/ws')

ws.onopen=()=>{ status.textContent='connected' }
ws.onmessage=(e)=>{
  const state=JSON.parse(e.data)
  if(state.type=='state') draw(state)
}

// steer toward the mouse
canvas.addEventListener('mousemove',(e)=>{
  const r=canvas.getBoundingClientRect()
  const dir=Math.atan2(e.clientY-r.top - 300, e.clientX-r.left - 400)
  if(ws.readyState==1) ws.send(JSON.stringify({type:'input', dir}))
})

function draw(state){
  ctx.clearRect(0,0,canvas.width,canvas.height)
  // TODO: draw the zone, food, power-ups, and snake bodies
  for(const s of state.snakes){
    ctx.fillStyle='#4caf50'
    ctx.beginPath()
    ctx.arc(s.x, s.y, 10, 0, 2*Math.PI)
    ctx.fill()
  }
}
