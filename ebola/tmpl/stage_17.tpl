


{% macro dialog() -%}
    Are you calling to report a possible case of Ebola?
    {{ caller() }}
{%- endmacro %}

{% macro input() -%}
<select name="is_ebola">
    <option>An Ebola Case</option>
    <option value="Y">Yes</option>
    <option value="N">No</option>
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

