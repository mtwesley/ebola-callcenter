


{% macro dialog() -%}
    Are you calling to ask about {% if patient -%} {{ patient }} {%- else -%} a patient {%- endif%}?
    {{ caller() }}
{%- endmacro %}

{% macro input() -%}
<select name="about_patient">
    <option>Asking About Patient</option>
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
