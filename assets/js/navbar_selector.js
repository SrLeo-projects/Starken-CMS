// Detect If .inline-related last-related dynamic-pagedetail_set to DOM

function hide_options(classname) {
    let sets = document.getElementsByClassName(classname);
    for (let i = 0; i < sets.length; i++) {
        let rows = sets[i].getElementsByClassName('form-group');
        let type_select = document.getElementById('id_navbardetail_set-'+[i]+'-type');
        if (type_select.value == 1) {
            rows[3].style.display = 'none';
        } else if (type_select.value == 2) {
            rows[1].style.display = 'none';
            rows[2].style.display = 'none';
        } else{
            rows[1].style.display = 'none';
            rows[2].style.display = 'none';
            rows[3].style.display = 'none';
        }
    }
}

$(document).ready(function() {
    
    setTimeout( function() {
        let errors = document.getElementsByClassName('errorlist nonfield');
        let classname = errors ? 'panel inline-related dynamic-navbardetail_set' : 'panel inline-related has_original dynamic-navbardetail_set';
        hide_options(classname);
    }, 1);

    
    $(document).on('DOMNodeInserted', function(e) {
        if ($(e.target).hasClass('panel inline-related last-related dynamic-navbardetail_set')) {
            // hide all .form-row fields except the first one
            $(e.target).find('.form-group').not(':first').hide();
            
            // get target id
            var target_id = $(e.target).attr('id');
            
            // add event listener to select
            $('#id_'+target_id+'-type').on('select2:select', function () {
                if (this.value == 1){
                    $(e.target).find('.form-group').show();
                    $(e.target).find('.form-group').first().show();
                    $(e.target).find('.form-group').last().hide();
                } else{
                    $(e.target).find('.form-group').hide();
                    $(e.target).find('.form-group').last().show();
                    $(e.target).find('.form-group').first().show();
                }
            });
        }
    });
});