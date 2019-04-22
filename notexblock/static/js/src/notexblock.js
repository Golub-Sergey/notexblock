/* Javascript for NoteXBlock. */
function NoteXBlock(runtime, element) {

    var handlerUrlAddNote = runtime.handlerUrl(element, 'add_note');

    function addNote(result){
        $('#note').val('')
        $('.notes', element).append(result['notes'] + '\n\n')
    }

    $('#note-submit', element).click(function (eventObject) {

        note = $('#note').val()

        data = {
            'note': note
        }
        console.log(data)

        $.ajax({
            type: "POST",
            url: handlerUrlAddNote,
            data: JSON.stringify(data),
            success: addNote
        })
    })

}
