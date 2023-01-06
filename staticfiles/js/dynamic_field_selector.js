// Detect If .inline-related last-related dynamic-pagedetail_set to DOM

$(document).ready(function() {
    // wait 1s
    setTimeout(function() {
        let sets = document.getElementsByClassName('panel inline-related has_original dynamic-pagedetail_set');
        console.log("hola");
        // for each set hide all .form-row whose selects without value
        for (let i = 0; i < sets.length; i++) {
            let rows = sets[i].getElementsByClassName('form-group');
            for (let j = 0; j < rows.length; j++) {
                let select = rows[j].getElementsByTagName('select')[0];
                if (select.value == '') {
                    rows[j].style.display = 'none';
                }
            }
        }
    }, 1);

    
    $(document).on('DOMNodeInserted', function(e) {
        if ($(e.target).hasClass('panel inline-related last-related dynamic-pagedetail_set')) {
            console.log(e.target)
            // hide all .form-row fields except the first one
            $(e.target).find('.form-group').not(':first').hide();
            
            // get target id
            var target_id = $(e.target).attr('id');
            
            // add event listener to select
            $('#id_'+target_id+'-type').on('select2:select', function () {
                $(e.target).find('.form-group').eq(this.value).show();
                $(e.target).find('.form-group').not(':eq(' + this.value + ')').hide();
                $(e.target).find('.form-group').first().show();
            });
        }
    });
});