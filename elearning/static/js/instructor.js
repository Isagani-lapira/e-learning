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