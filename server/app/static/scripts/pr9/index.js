document.addEventListener('DOMContentLoaded', () => {
    const search_btn = document.getElementById('search-btn');
    search_btn.addEventListener("click", getBankData);
    const div_table = document.getElementById('data-table');

    function getBankData(e) {
        let inputVal = document.getElementById('field1').value;
        console.log(inputVal);
        fetch(`get_fin_data?field1=${inputVal}`)
            .then(response => response.json())
            .then(data_json => {
                if (data_json.data) {
                    show_data(data_json);
                } else {
                    div_table.innerHTML = 'Ошибка поиска'
                }
            });
    }

    function show_data(data_json) {
        div_table.innerHTML = '';
        let div_header = document.createElement('div');
        div_header.className = 'fw-bold';
        div_header.innerText = 'Реквизиты ' + data_json.value;
        div_table.append(div_header);
        let table = document.createElement('table');
        table.className = 'table';
        let table_body = document.createElement('tbody');
        table_body.append(create_row('Наименование банка', data_json.data.name.short));
        table_body.append(create_row('Юридический адрес', data_json.data.address.value));
        table_body.append(create_row('Корр. счет', data_json.data.correspondent_account));
        table_body.append(create_row('БИК', data_json.data.bic));
        table_body.append(create_row('SWIFT', data_json.data.swift));

        table.append(table_body);
        div_table.append(table);
    }

    function create_row(name, value) {
        let tr = document.createElement('tr');
        let td_name = document.createElement('td');
        td_name.innerText = name;
        let td_value = document.createElement('td');
        td_value.innerText = value;
        tr.append(td_name);
        tr.append(td_value);
        return tr
    }
});