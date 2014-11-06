
{% macro dialog() -%}
    What is your primary language?
    {{ caller() }}
{%- endmacro %}

{% macro input() -%}
<select name="lang">
    <option value="English">English</option>
    <option value="Kisi">Kisi </option>
    <option value="Manding">Manding</option>
    <option value="Kru">Kru</option>
    <option value="Gola">Gola</option>
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

