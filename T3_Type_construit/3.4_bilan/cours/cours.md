# Fiche bilan : Types construits 

Cette fiche bilan n'est pas exhaustive ! Libre à vous de rajouter des éléments !

<table style="text-align:center" border='1px' width=100%>
    <tr>
        <td width=5% > </td>
        <td width=10%> </td>
        <td width=14%> <center><b> Tuple</b></center> </td>
        <td width=14%> <center><b> Liste</b></center> </td>
        <td width=14%> <center><b> Dictionnaire</b></center> </td>
        <td width=14%> <center><b> Listes de listes</b></center> </td>
        <td width=35%> <center><b> Description</b></center> </td>
    </tr>
    <tr>
        <td width=10% rowspan ="5">    <center><b>C<br>a<br>r<br>a<br>c<br>t<br>é<br>r<br>i<br>s<br>t<br>i<br>q<br>u<br>e<br>s<br> </b></center></td>
        <td> De tout type ? </td>
        <td> <center><font color="FF0000">OUI</font></center> </td>
        <td> <center>OUI</center></td>
        <td> <center>Non pour les clés <br>Oui pour les valeurs</center></td>
        <td> <center>OUI</font></td>
        <td> <center><font color="FF0000">Peut contenir des nombres entiers, des réels, des booléens, des chaînes de caractères, ...</font></center></td>
    </tr>
    <tr>
        <td> Ordonné ? </td>
        <td> <center><font color="FF0000">OUI</font></center></td>
        <td> <center>OUI</center></td>
        <td> <center>NON mais les logiciels s'en chargent parfois</center></td>
        <td> <center>OUI</center></td>
        <td><center><font color="FF0000">Les éléments sont conservés dans l'ordre</font></center> </td>
    </tr>
    <tr>
        <td> Indexable ? </td>
        <td> <center><font color="FF0000">OUI</font></center></td>
        <td> <center>OUI</center></td>
        <td> <center>OUI grâce aux clés</center></td>
        <td> <center>OUI</center></td>
        <td> <center><font color="FF0000">Chaque élément est accessible grâce à son index</font></center></td>
    </tr>
    <tr>
        <td> Itérable ? </td>
        <td> <center><font color="FF0000">OUI</font></center></td>
        <td> <center>OUI</center></td>
        <td> <center>OUI</center></td>
        <td> <center>OUI</center></td>
        <td> <center><font color="FF0000">Il est possible de parcourir les éléments grâce à une boucle for par exemple</font></center></td>
    </tr>
    <tr>
        <td> Mutable ? </td>
        <td> <center><font color="FF0000">NON</font></center></td>
        <td> <center>OUI</center></td>
        <td> <center>OUI seulement pour les valeurs</center></td>
        <td> <center>OUI</center></td>
        <td> <center><font color="FF0000">Il est possible de modifier les éléments déjà présents</font></center></td>
    </tr>
     <tr>
         <td width=10% rowspan ="15"> <center><b>O<br>p<br>é<br>r<br>a<br>t<br>i<br>o<br>n<br>s</b></center> </td>
        <td> <center><b>in</b></center> </td>
        <td> <center><font color="FF0000">OUI</font></center></td>
        <td> <center>OUI</center></td>
        <td> <center>OUI</center></td>
        <td> <center>OUI</center></td>
        <td> <center><font color="FF0000">Permet de savoir si un élément est présent</font></center></td>
    </tr>
     <tr>
        <td><center><b>len</b></center> </td>
        <td> <center><font color="FF0000">OUI</font></center></td>
        <td> <center>OUI</center></td>
        <td> <center>OUI</center></td>
        <td> <center>OUI</center></td>
        <td> <center><font color="FF0000">Permet de connaître le nombre d'éléments</font></center></td>
    </tr>
     <tr>
         <td><center><b>index</b></center> </td>
        <td> <center><font color="FF0000">OUI</font></center></td>
        <td> <center>OUI</center></td>
        <td> <center>NON</center></td>
        <td> <center>OUI</center></td>
        <td> <center><font color="FF0000">Permet de connaître l'index de l'élément</font></center></td>
    </tr>
     <tr>
        <td> <center>Slice [i : j]</center> </td>
        <td> <center><font color="FF0000">OUI</font></center></td>
        <td> <center>OUI</center></td>
        <td> <center>NON</center></td>
        <td> <center>OUI</center></td>
        <td> <center><font color="FF0000">Renvoie une partie des éléments de l’indice i à j non inclus</font></td>
    </tr>
     <tr>
         <td><center><b>count</b></center> </td>
        <td> <center><font color="FF0000">OUI</font></center></td>
        <td> <center>OUI</center></td>
        <td> <center>NON</center></td>
        <td> <center>OUI</center></td>
        <td> <center><font color="FF0000">Renvoie le nombre d'apparitions d'un élément</font></center></td>
    </tr>
     <tr>
         <td><center> Concaténation <b>+</b></center></td>
        <td> <center><font color="FF0000">OUI</font></center></td>
        <td> <center>OUI</center></td>
        <td> <center>NON</center></td>
        <td> <center>OUI</center></td>
        <td> <center><font color="FF0000">Renvoie une nouvelle séquence à partir de deux séquences</font></center></td>
    </tr>
     <tr>
        <td> <center><b>append</b> </center> </td>
        <td> <center><font color="FF0000">NON</font></center></td>
        <td> <center>OUI</center></td>
        <td> <center>NON</center></td>
        <td> <center>OUI</center></td>
        <td> <center>Ajoute un élément (à la fin)</center></td>
    </tr>
     <tr>
         <td><center><b>remove</b></center> </td>
        <td> <center><font color="FF0000">NON</font></center></td>
        <td> <center>OUI</center></td>
        <td> <center>NON</center></td>
        <td> <center>OUI</center></td>
        <td> <center>Supprime la première apparition d'un élément</center></td>
    </tr>
     <tr>
         <td><center><b>insert</b></center> </td>
        <td> <center><font color="FF0000">NON</font></center></td>
        <td> <center>OUI</center></td>
        <td> <center>NON</center></td>
        <td> <center>OUI</center></td>
        <td> <center>Insère un élément grâce à son index</center></td>
    </tr>
     <tr>
         <td><center><b>pop</b></center> </td>
        <td> <center><font color="FF0000">ON</font></center></td>
        <td> <center>OUI</center></td>
        <td> <center>OUI</center></td>
        <td> <center>OUI</center></td>
        <td> <center>Supprime un élément grâce à son index (ou clé)</center></td>
    </tr>
     <tr>
         <td><center><b>sort</b></center> </td>
        <td> <center><font color="FF0000">NON</font></center></td>
        <td> <center>OUI</center></td>
        <td> <center>NON</center></td>
        <td> <center>OUI</center></td>
        <td> <center>Permet de trier</center></td>
    </tr>
     <tr>
         <td><center><b>keys</b></center> </td>
        <td> <center><font color="FF0000">NON</font></center></td>
        <td> <center>NON</center></td>
        <td> <center>OUI</center></td>
        <td> <center>NON</center></td>
        <td> <center>Permet de chercher parmi les clés</center></td>
    </tr>
     <tr>
         <td><center><b>values</b></center> </td>
        <td> <center><font color="FF0000">NON</font></center></td>
        <td> <center>NON</center></td>
        <td> <center>OUI</center></td>
        <td> <center>NON</center></td>
        <td> <center>Permet de chercher parmi les valeurs</center></td>
    </tr>
     <tr>
         <td><center><b>items</b></center> </td>
        <td> <center><font color="FF0000">NON</font></center></td>
        <td> <center>NON</center></td>
        <td> <center>OUI</center></td>
        <td> <center>NON</center></td>
        <td> <center>Permet de chercher parmi les clés et les valeurs</center></td>
    </tr>
    <tr>
         <td><center><b>get</b></center> </td>
        <td> <center><font color="FF0000">NON</font></center></td>
        <td> <center>NON</center></td>
        <td> <center>OUI</center></td>
        <td> <center>NON</center></td>
        <td> <center>Renvoie la valeur associé à une clé</center></td>
    </tr>

      
</table>