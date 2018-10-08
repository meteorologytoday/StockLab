<style type="text/css">
table {
    border-width:2px;
    border-style: solid;
    border-collapse:collapse;
    border-spacing:0;
}

td {
    padding: 3px;
}

tr:hover{
    background-color: #ccc;
}
</style>
<table style="border-width:2px; border-style: solid; border-collapse:collapse; border-spacing:0 ">
<tr>
    <th>No</th>
    <th>Symbol</th>
    <th>Exchange</th>
    <th>Avg Price</th>
    <th>Long Term Trend (20d)</th>
    <th>Short Term Trend (5d)</th>
    <th>Shortwave relative strength</th>
    <th>Variability</th>
</tr>
% for i, row in data.iterrows():
%   link = "https://finance.yahoo.com/chart/%s" % row['Symbol']
    <tr>
        <td>{{i}}</td>
        <td><a href="{{link}}" target="_blank">{{row['Symbol']}}</a></td>
        <td>{{row['Exchange']}}</td>
        <td>{{row['Avg_price']}}</td>
        <td>{{row['Long_term_slope']}}</td>
        <td>{{row['Short_term_slope']}}</td>
        <td>{{row['shortwave_relative_power']}}</td>
        <td>{{row['Variability']}}</td>
    </tr>
% end

</table>
