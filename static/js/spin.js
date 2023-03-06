

const open_modal = document.getElementById('close');
const bg_modal = document.getElementById('bg-modal');
const btn_modal = document.getElementById('btn');

const small_up = document.getElementById('add_small');
const small_down = document.getElementById('sub_small');

const med_up = document.getElementById('add_med');
const med_down = document.getElementById('sub_med');

const large_up = document.getElementById('add_lar');
const large_down = document.getElementById('sub_lar');




var open_ = false


small_up.addEventListener("click", ()=>{
    let val = document.getElementById('spq').value;
    document.getElementById("spq").value = Number(val)+1;
})

small_down.addEventListener("click", ()=>{
    let val = document.getElementById('spq').value;
    if(val >= 1){
        document.getElementById("spq").value = Number(val)-1;
    }
})




med_up.addEventListener("click", ()=>{
    let val = document.getElementById('mpq').value;
    document.getElementById("mpq").value = Number(val)+1;
})

med_down.addEventListener("click", ()=>{
    let val = document.getElementById('mpq').value;
    if(val >= 1){
        document.getElementById("mpq").value = Number(val)-1;
    }
})





large_up.addEventListener("click", ()=>{
    let val = document.getElementById('lpq').value;
    document.getElementById("lpq").value = Number(val)+1;
})

large_down.addEventListener("click", ()=>{
    let val = document.getElementById('lpq').value;
    if(val >= 1){
        document.getElementById("lpq").value = Number(val)-1;
    }
})





btn_modal.addEventListener("click", ()=>{
    if (open_ == true){
        bg_modal.style.display = 'none';
        open_ = false;
    }
    else{
        bg_modal.style.display = 'flex';
        open_ = true;
    }
})


open_modal.addEventListener("click", ()=>{
    if (open_ == true){
        bg_modal.style.display = 'none';
        open_ = false;
    }
    else{
        bg_modal.style.display = 'flex';
        open_ = true;
    }

})