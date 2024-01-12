function deleteCourse(){
    $('#delete_course_form').on('submit',function(e){
        e.preventDefault()

        Swal.fire({
            title: 'Delete Course!',
            text: 'Are you sure you want to delete this course?',
            icon: 'error',
            showCancelButton: true,
            confirmButtonColor: '#F35F5F',
            cancelButtonColor: '#D0D0D0',
          }).then(result=>{
                // remove course
                if(result.isConfirmed){
                    $('#delete_course_form')[0].submit();
                }
          })
    })
}


function deleteModuleData(id,isModule){
    
    Swal.fire({
        title: 'Delete Module',
        text: `Are you sure you want to delete this ${(isModule)? "Module":"Lesson"}?`,
        icon: 'error',
        showCancelButton: true,
        confirmButtonColor: '#F35F5F',
        cancelButtonColor: '#D0D0D0',
    }).then(result=>{
        if(result.isConfirmed){
            if(isModule)
                $('#deleteModalForm_'+id).submit() //delete a form of specific module
            else
                $('#delLesson_'+id).submit()// delete lesson in module
        }
    })
}
// toggle course modal
function NewCourseModal(action){

    if (action === 'open')
        $('.modal').removeClass('hidden')
    else $('.modal').addClass('hidden')
}


$(function() {
    $("#accordion").accordion({
      collapsible: true,
      active: false, // Set to the index of the initially open section, or false to close all by default
      heightStyle: "content",
      activate: function(event, ui) {
        $(".ui-state-active").removeClass("ui-state-active").addClass('bg-primary');
        ui.newHeader.addClass("bg-primary");
      }
    });
});