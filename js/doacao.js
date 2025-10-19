function showErr(el,msg){
  const s = el.closest('.field')?.querySelector('.error');
  if(s) s.textContent = msg || '';
  el.setAttribute('aria-invalid', msg ? 'true' : 'false');
}
function clamp(v,min,max){ return Math.max(min, Math.min(max, v)); }

const dia = document.getElementById('dia');
const mes = document.getElementById('mes');
const ano = document.getElementById('ano');
[dia,mes,ano].forEach(el=>{
  el.addEventListener('input', ()=>{
    if(el===dia) el.value = el.value ? clamp(+el.value,1,31) : '';
    if(el===mes) el.value = el.value ? clamp(+el.value,1,12) : '';
    if(el===ano) el.value = el.value ? clamp(+el.value,2025,2100) : '';
  });
});

document.getElementById('form-doacao').addEventListener('submit', (e)=>{
  e.preventDefault();

  const quantia = document.getElementById('quantia');
  const local = document.getElementById('local');

  [quantia,dia,mes,ano,local].forEach(i=>showErr(i,''));

  let ok = true;
  if(!quantia.value || +quantia.value < 50){ showErr(quantia,'Informe a quantia (mín. 50 ml)'); ok=false; }
  const d = +dia.value, m = +mes.value, a = +ano.value;
  const dataValida = d>=1 && d<=31 && m>=1 && m<=12 && a>=2025 && a<=2100;
  if(!dataValida){ showErr(ano,'Data inválida'); ok=false; }
  if(!local.value){ showErr(local,'Selecione um local'); ok=false; }

  if(!ok) return;

  const payload = {
    quantia: Number(quantia.value),
    data: `${String(d).padStart(2,'0')}/${String(m).padStart(2,'0')}/${a}`,
    local: local.value
  };

  // Persistir no navegador como demo; substitua por POST ao backend
  const key = 'sang_agendamentos';
  const arr = JSON.parse(localStorage.getItem(key) || '[]');
  arr.push({...payload, ts: Date.now()});
  localStorage.setItem(key, JSON.stringify(arr));

  alert('Doação agendada com sucesso! (demo)');
  location.href = '/';
});
