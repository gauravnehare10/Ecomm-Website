const qty = document.querySelector(".qty-input");
    
    
    document.querySelector(".decrement-btn").onclick = function(){
        if(qty.value > 1){
            qty.value-=1;
        }
    }
    document.querySelector(".increment-btn").onclick = function(){
        if(qty.value < 10){
            qty.value= +qty.value+1;
        }
    }

document.querySelector(".addtocartbtn").onclick = () =>{
    var product_id = document.querySelector(this).closest(".product_data").find(".prod_id").val();
    var product_qty = document.querySelector(this).closest(".product_data").find(".qty-input").val();
    

}
