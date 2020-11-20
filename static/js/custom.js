document.querySelector('#form').addEventListener("submit", e => {
    e.preventDefault()
    let code = getGraphCode()

    location.search.code = code
})

let x = document.querySelector('#x')
let y = document.querySelector('#y')
let condition = document.querySelector('#condition')
let age_lower = document.querySelector('#age_lower')
let age_upper = document.querySelector('#age_upper')
let zone = document.querySelector('#zone')
let time_lower = document.querySelector('#time_lower')
let time_upper = document.querySelector('#time_upper')


function getGraphCode () {
    let x_value = x.value
    let y_value = y.value
    let condition_value = condition.value
    let zone_value = zone.value

    let age = enforce_length(age_lower.value, 2)
    age += enforce_length(parseInt(age_upper.value)+1, 2)

    let time = enforce_length(time_lower.value, 3)
    time += enforce_length(parseInt(time_upper.value)+1, 3)
    
    return [ x_value, y_value, condition_value, zone_value, age, time ].join('-')
}

function enforce_length (val, len) {
    let vallen = val.length

    for (let i = vallen ; i<len ; i++) 
        val = "0" + val

    return val
}

x.onchange = e => {
    if (x.value == '0') { // over age
        // age_lower.value = 0
        // age_upper.value = 89
        // age_lower.disabled = true
        // age_upper.disabled = true
        
        // time_lower.disabled = false
        // time_upper.disabled = false
        
        
        zone.disabled = false
        condition.disabled = false

        y.children[3].disabled = true  // infection rate
        if (y.value == '3') {
            y.value = '0'
            age_lower.disabled = false
            age_upper.disabled = false
        }
    } 

    else if (x.value == '1') { // over time infected
        // time_lower.value = 0
        // time_upper.value = 238
        // time_lower.disabled = true
        // time_upper.disabled = true
        
        // age_lower.disabled = false
        // age_upper.disabled = false
        
        zone.disabled = false
        condition.disabled = false

        y.children[3].disabled = true  // infection rate
        if (y.value == '3') {
            y.value = '0'
            age_lower.disabled = false
            age_upper.disabled = false
        }
    } 

    else if (x.value == '2') { // over population density
        zone.value = 400
        condition.value = '0'
        zone.disabled = true
        condition.disabled = true
        
        // time_lower.disabled = false
        // time_upper.disabled = false
        
        // age_lower.disabled = false
        // age_upper.disabled = false

        age_lower.value = 0
        age_upper.value = 89
        time_lower.value = 0
        time_upper.value = 238

        y.children[3].disabled = false // infection rate
    }
}

y.onchange = e => {
    if (y.value == '3') {
        age_lower.value = 0
        age_upper.value = 89
        age_lower.disabled = true
        age_upper.disabled = true
    }
    else {
        age_lower.disabled = false
        age_upper.disabled = false
    }
}

age_lower.onchange = e => {
    if (parseInt(age_upper.value) <= parseInt(age_lower.value))
        age_upper.value = parseInt(age_lower.value) + 1
    
    age_upper.min = parseInt(age_lower.value) + 1

    if (x.value == '2') {
        time_lower.value = 0
        time_upper.value = 238
    }
}

age_upper.onchange = e => {
    if (x.value == '2') {
        time_lower.value = 0
        time_upper.value = 238
    }
}

time_lower.onchange = e => {
    if (parseInt(time_upper.value) <= parseInt(time_lower.value))
        time_upper.value = parseInt(time_lower.value) + 1
    
    time_upper.min = parseInt(time_lower.value) + 1 

    if (x.value == '2') {
        age_lower.value = 0
        age_upper.value = 89
    }
}

time_upper.onchange = e => {
    if (x.value == '2') {
        age_lower.value = 0
        age_upper.value = 89
    }
}