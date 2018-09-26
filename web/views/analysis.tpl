
<table>
<tr>
    <th>No</th>
    <th>Symbol</th>
    <th>Avg_Price</th>
</tr>
% for i, row in data.iterrows():
%   link = "https://finance.yahoo.com/chart/%s" % row['Symbol']
    <tr>
        <td>{{i}}</td>
        <td><a href="{{link}}" target="_blank">{{row['Symbol']}}</a></td>
        <td>{{row['Avg_price']}}</td>
    </tr>
% end

</table>
