function tmify(item) {
    if (item.textContent) {
        item.textContent = item.textContent.split(' ').map(bit => tmifier(bit)).join(' ')
    }
    Array.from(item.children).forEach(item => {
        if (item.children && item.children.length) {
            return tmify(item)
        }
    })
}

function tmifier(bit) {
    // different rules
    if (bit && bit.length == 6) {
        return `${bit}™`
    } else {
        return bit
    }
}

document.querySelectorAll("div.comment > span.commtext").forEach(item => tmify(item))