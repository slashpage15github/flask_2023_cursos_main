$(document).ready(function() {
    $("#f_rfc").blur(function(){
        let x_rfc=document.getElementById("f_rfc").value.trim().toUpperCase();
        if(x_rfc!= '')  
        {  
             $.ajax({  
                  url:'/valida_existe',  
                  method:'POST',  
                  data:{x_rfc:x_rfc},  
                  success:function(response){
                         //alert(response);
                         if (response==1){
                            mensaje('error','Registro duplicado','El Aspirante ya se encuentra registrado!',null);
                         }  
                       
                  },
                 error : function(request, status, error) {

                         var val = request.responseText;
                         alert("error"+val);
                 }  
             });  
        }
        else{
            mensaje('error','No  llegó RFC','verificar RFC!',null);
        } 
        
      });
});