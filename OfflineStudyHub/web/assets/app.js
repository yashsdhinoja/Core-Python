const groups = [
  {key:"react-project", title:"React Project", path:"/materials/react-project/"},
  {key:"dsa-python", title:"DSA in Python", path:"/materials/dsa-python/"},
  {key:"advanced-dbms", title:"Advanced DBMS", path:"/materials/advanced-dbms/"}
];
const list = document.getElementById("file-list");
const search = document.getElementById("search");
let allRows = [];

function esc(s){return String(s).replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));}
function iconFor(name){
  const ext = name.includes(".") ? name.split(".").pop().toLowerCase() : "DIR";
  return ({pdf:"PDF",py:"PY",html:"HTML",htm:"HTML",js:"JS",jsx:"JS",tsx:"TS",ts:"TS",css:"CSS",md:"MD",txt:"TXT",docx:"DOC",doc:"DOC",pptx:"PPT",xlsx:"XLS",png:"IMG",jpg:"IMG",jpeg:"IMG",mp4:"VID"})[ext] || ext.slice(0,4).toUpperCase();
}
async function loadGroup(group){
  const res = await fetch("/api/files?section="+encodeURIComponent(group.key));
  if(!res.ok) throw new Error("Could not load "+group.title);
  return await res.json();
}
function render(){
  const q=search.value.trim().toLowerCase();
  const visible=allRows.map(g=>({...g,files:g.files.filter(f=>(g.title+" "+f.name+" "+f.path).toLowerCase().includes(q))}));
  list.innerHTML=visible.map(g=>{
    const body=g.files.length ? g.files.map(f=>`<div class="file-row"><span class="file-symbol">${esc(iconFor(f.name))}</span><div class="file-meta"><span class="file-name">${esc(f.name)}</span><span class="file-path">${esc(f.path)}</span></div><a class="file-action" href="${esc(f.url)}" target="_blank" rel="noopener">Open ↗</a></div>`).join("") : `<div class="empty">${q?"No matching files.":"No files yet. Copy files into this section's folder."}</div>`;
    return `<section class="file-group" id="${esc(g.key)}"><div class="group-title"><span>${esc(g.title)}</span><span>${g.files.length} file${g.files.length===1?"":"s"}</span></div>${body}</section>`;
  }).join("");
}
async function refresh(){
  list.innerHTML='<div class="loading">Reading local folders…</div>';
  try{
    allRows=await Promise.all(groups.map(async g=>({key:g.key,title:g.title,files:await loadGroup(g)})));
    render();
  }catch(e){list.innerHTML='<div class="empty">Could not read the file list. Restart the Python server and refresh.</div>';}
}
search.addEventListener("input",render);
document.getElementById("refresh").addEventListener("click",refresh);
refresh();
