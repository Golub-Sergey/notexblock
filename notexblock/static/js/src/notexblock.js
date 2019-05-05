/* Javascript for NoteXBlock. */
function NoteXBlock(runtime, element) {

    var handlerUrlAddNote = runtime.handlerUrl(element, 'add_note');

    function addNote(result){
        $('.notes', element).val(result['notes'])
    }

    $('#note-submit', element).click(function (eventObject) {

        notes = $('.notes').val()

        data = {
            'notes': notes
        }
        $.ajax({
            type: "POST",
            url: handlerUrlAddNote,
            data: JSON.stringify(data),
            success: addNote
        })
    })

    $(document).ready(function() {
        $('.notes').froalaEditor({
            width: 350,
            height: 300
        })
    });


}
