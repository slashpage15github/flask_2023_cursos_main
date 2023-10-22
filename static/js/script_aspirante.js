$(document).ready(function() {
    $("#f_rfc").blur(function(){
        let f_rfc=document.getElementById("f_rfc").value.trim().toUpperCase();
        alert(f_rfc);
        if(f_rfc!= '')  
        {  
             $.ajax({  
                  url:'/valida_existe',  
                  method:'POST',  
                  data:{f_rfc:f_rfc},
                  success:function(response){
                         //alert(response);
                         console.log(response)
                         if (response==1){
                            //alert('pendejo');
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