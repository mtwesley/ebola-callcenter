


{% macro dialog() -%}
    What county are you calling from?
    {{ caller() }}
{%- endmacro %}

{% macro input() -%}
<select name="county">
    <option value="Bomi">Bomi</option>
    <option value="Bong">Bong</option>
    <option value="Gbarpolu">Gbarpolu</option>
    <option value="Grand Bassa">Grand Bassa</option>
    <option value="Grand Cape Mount">Grand Cape Mount</option>
    <option value="Grand Gedeh">Grand Gedeh</option>
    <option value="Grand Kru">Grand Kru</option>
    <option value="Lofa">Lofa</option>
    <option value="Margibi">Margibi</option>
    <option value="Maryland">Maryland</option>
    <option value="Montserrado">Montserrado</option>
    <option value="Nimba">Nimba</option>
    <option value="Rivercess">Rivercess</option>
    <option value="River Gee">River Gee</option>
    <option value="Sinoe">Sinoe</option>
</select>
{{ caller() }}
{%- endmacro %}

{% macro cancel() -%}
<a class="btn gradient_red rounded" href="{{ url_for('_ui.index') }}">
    CANCEL CALL
</a>
{{ caller() }}
{%- endmacro %}


{% include "call_0.tpl" %}
