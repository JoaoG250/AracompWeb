const converter = new showdown.Converter()
$('.markdown-body').each(function () {
    const content = $(this).text().trim()
    $(this).html(converter.makeHtml(content))
    $(this).show()
})
$('.ver-mais-btn').on('click', function () {
    const target = $($(this).data('target'))
    if (target.data('expanded')) {
        target.data('expanded', false)
        $(this).html('Ver mais')
    } else {
        target.data('expanded', true)
        $(this).html('Ver menos')
    }
    target.slideToggle()
})