function add_belt_shelf() {
        $('#batterie_shelf').hide();
        $('#electric_shelf').hide();
        $('#id_shelf_type').val('belt');
        var counter = $('.belts').length;
        counter = (parseFloat(counter) / 3) + 1;
        var char = 'belt_shelf_char_' + counter;
        var id_char = 'belt_id_shelf_char_' + counter;
        var num = 'belt_shelf_num_' + counter;
        var id_num = 'belt_id_shelf_num_' + counter;
        $('.shelfs > tbody > tr').append("<td class='belts'>"+
        '<select name="' + char + '" id="' + id_char + '" >'+
            '<option>A</option>'+
            '<option>B</option>'+
            '<option>C</option>'+
            '<option>D</option>'+
            '<option>E</option>'+
            '<option>F</option>'+
            '<option>G</option>'+
            '<option>H</option>'+
            '<option>K</option>'+
            '<option>M</option>'+
            '<option>N</option>'+
            '<option>O</option>'+
            '<option>P</option>'+
            '<option>Q</option>'+
            '<option>R</option>'+
            '<option>S</option>'+
            '<option>T</option>'+
            '<option>V</option>'+
            '<option>W</option>'+
            '<option>X</option>'+
            '<option>Y</option>'+
            '<option>Z</option>'+
        '</select>'+
        '</td><td>'+
        '<select name="' + num + '" id="' + id_num + '" >'+
            '<option value="1">1</option>'+
            '<option value="2">2</option>'+
            '<option value="3">3</option>'+
            '<option value="4">4</option>'+
        '</select>'+
        '</td><td>' + counter.toString() + '</td>')
        $('#id_num_of_rows').val(counter);
    }

    function add_batterie_shelf() {
        $('#belt_shelf').css('visibility', 'hidden');
        $('#electric_shelf').hide();
        $('#id_shelf_type').val('.batteries');
        var counter = $('.batteries').length;
        counter = (parseFloat(counter) / 3) + 1;
        var char = 'batterie_shelf_char_' + counter;
        var id_char = 'batterie_id_shelf_char_' + counter;
        var num = 'batterie_shelf_num_' + counter;
        var id_num = 'batterie_id_shelf_num_' + counter;
        $('.shelfs > tbody > tr').append("<td class='batteries'>"+
        '<select name="' + char + '" id="' + id_char + '" >'+
            '<option>A</option>'+
            '<option>B</option>'+
            '<option>C</option>'+
            '<option>D</option>'+
            '<option>E</option>'+
            '<option>F</option>'+
            '<option>G</option>'+
            '<option>H</option>'+
            '<option>K</option>'+
            '<option>M</option>'+
            '<option>N</option>'+
            '<option>O</option>'+
            '<option>P</option>'+
            '<option>Q</option>'+
            '<option>R</option>'+
            '<option>S</option>'+
            '<option>T</option>'+
            '<option>V</option>'+
            '<option>W</option>'+
            '<option>X</option>'+
            '<option>Y</option>'+
            '<option>Z</option>'+
        '</select>'+
        '</td><td>'+
        '<select name="' + num + '" id="' + id_num + '" >'+
            '<option>1</option>'+
            '<option>2</option>'+
            '<option>3</option>'+
            '<option>4</option>'+
        '</select>'+
        '</td><td>' + counter.toString() + '</td>')
        $('#id_num_of_rows').val(counter);
    }

    function add_electric_shelf() {
        $('#belt_shelf').css('visibility', 'hidden');
        $('#batterie_shelf').css('visibility', 'hidden');
        $('#id_shelf_type').val('electric');
        var counter = $('.electrics').length;
        counter = (parseFloat(counter) / 3) + 1;
        var char = 'electric_shelf_char_' + counter;
        var id_char = 'electric_id_shelf_char_' + counter;
        var num = 'electric_shelf_num_' + counter;
        var id_num = 'electric_id_shelf_num_' + counter;
        $('.shelfs > tbody > tr').append("<td class='electrics'>"+
        '<select name="' + char + '" id="' + id_char + '" >'+
            '<option>A</option>'+
            '<option>B</option>'+
            '<option>C</option>'+
            '<option>D</option>'+
            '<option>E</option>'+
            '<option>F</option>'+
            '<option>G</option>'+
            '<option>H</option>'+
            '<option>K</option>'+
            '<option>M</option>'+
            '<option>N</option>'+
            '<option>O</option>'+
            '<option>P</option>'+
            '<option>Q</option>'+
            '<option>R</option>'+
            '<option>S</option>'+
            '<option>T</option>'+
            '<option>V</option>'+
            '<option>W</option>'+
            '<option>X</option>'+
            '<option>Y</option>'+
            '<option>Z</option>'+
        '</select>'+
        '</td><td>'+
        '<select name="' + num + '" id="' + id_num + '" >'+
            '<option>1</option>'+
            '<option>2</option>'+
            '<option>3</option>'+
            '<option>4</option>'+
        '</select>'+
        '</td><td>' + counter.toString() + '</td>')
        $('#id_num_of_rows').val(counter);
    }