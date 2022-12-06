document.addEventListener('DOMContentLoaded', () => {
    const input = document.getElementById('field1');
    input.addEventListener('keyup', getMatches);
    const suggestions = document.querySelector('.suggestions ul');
    suggestions.addEventListener('click', useSuggestion);
    const div_table = document.getElementById('data-table');

    let addresses = [];

    function getMatches(elem) {
        const inputVal = elem.currentTarget.value;
        fetch(`./get_address?field1=${inputVal}`)
            .then(response => response.json())
            .then(matches_json => {
                showSuggestions(matches_json);
            });
    }

    function showSuggestions(results) {
        suggestions.innerHTML = '';
        addresses = results;
        if (results.length > 0) {
            for (let i = 0; i < results.length; i++) {
                let li_new = document.createElement('div');
                li_new.className = 'list-group-item list-group-item-action';
                li_new.innerHTML = `${results[i].value}`;
                li_new.id = `adr-${i}`;
                suggestions.append(li_new);
            }
        } else {
            suggestions.innerHTML = '';
        }
    }

    function useSuggestion(e) {
        input.value = e.target.innerHTML;
        let address_idx = e.target.id.slice(4);
        showAddressDetails(addresses[address_idx]);
    }

    function showAddressDetails(address_data) {
        div_table.innerHTML = '';
        let table = document.createElement('table');
        table.className = 'table';
        let table_body = document.createElement('tbody');
        table_body.append(create_row('Адрес:', address_data.value));
        table_body.append(create_row('Индекс:', address_data.data.postal_code));
        table_body.append(create_row('Код ФИАС:', address_data.data.fias_id));
        table_body.append(create_row('Код КЛАДР:', address_data.data.kladr_id));

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