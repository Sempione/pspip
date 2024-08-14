<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE TS>
<TS version="2.1" language="de">
<context>
    <name>PutSpacedPointsInPolygonsAlgorithm</name>
    <message>
        <location filename="../pspip_algorithm.py" line="82"/>
        <source>Input layer</source>
        <translation>Eingabelayer</translation>
    </message>
    <message>
        <location filename="../pspip_algorithm.py" line="93"/>
        <source>Fitted_point_grids</source>
        <translation>Eingepasste_Punkte</translation>
    </message>
    <message>
        <location filename="../pspip_algorithm.py" line="101"/>
        <source>Distance between points</source>
        <translation>Abstand zwischen den Punkten</translation>
    </message>
    <message>
        <location filename="../pspip_algorithm.py" line="111"/>
        <source>Number of iterations (x-direction)</source>
        <translation>Anzahl der Schritte (x-Richtung)</translation>
    </message>
    <message>
        <location filename="../pspip_algorithm.py" line="123"/>
        <source>Number of iterations (y-direction)</source>
        <translation>Anzahl der Schritte (y-Richtung)</translation>
    </message>
    <message>
        <location filename="../pspip_algorithm.py" line="135"/>
        <source>Number of iterations (rotation)</source>
        <translation>Anzahl der Schritte (Rotation)</translation>
    </message>
    <message>
        <location filename="../pspip_algorithm.py" line="147"/>
        <source>Grid types to use</source>
        <translation>Zu verwendende Gittertypen</translation>
    </message>
    <message>
        <location filename="../pspip_algorithm.py" line="147"/>
        <source>only triangle based grids</source>
        <translation>nur auf Dreiecken basierende Gitter</translation>
    </message>
    <message>
        <location filename="../pspip_algorithm.py" line="147"/>
        <source>only square based grids</source>
        <translation>nur auf Quadraten basierende Gitter</translation>
    </message>
    <message>
        <location filename="../pspip_algorithm.py" line="147"/>
        <source>both triangle and square based grids</source>
        <translation>sowohl auf Dreiecken als auch auf Quadraten basierende Gitter</translation>
    </message>
    <message>
        <location filename="../pspip_algorithm.py" line="424"/>
        <source>Put spaced points in polygons</source>
        <translation>Punkte mit Abstand in Polygone setzen</translation>
    </message>
    <message>
        <location filename="../pspip_algorithm.py" line="432"/>
        <source>This algorithm takes a polygon layer and asks you to enter                       a &quot;Distance between points&quot; value. Taking the distance constraint                        into account, it attempts to find an arrangement of points within                        each polygon that yields the highest possible number of points                        (note the caveat in the following paragraph). The algorithm outputs                        a multipoint layer containing one feature for each feature from the                        input layer. Its attributes are an &quot;FID&quot; (int) field referring to                        the input feature&apos;s fid and a &quot;NUMPOINTS&quot; (int) field stating the                        number of points that were fitted. The multipoint geometry contains                        an arrangement of points that yielded the highest number of points.                       

Please bear in mind that this is an approximation algorithm that                        is based on testing a large number of possible point arrangements.                        This approach does not make it possible to find the very best                        solution with certainty.

The basis for the testing process are                        regular point grids. You can choose whether you would like the                        algorithm to use square based grids, triangle based grids or both.                        Please note that square based grids provide the optimum result only                        in special cases (relatively small, rectangular input polygons).                       

The algorithm takes the grids and varies them by moving them                        step by step in the x-direction and y-direction and rotating them                        (and all of them at the same time). You can specify how many                        iterations you want to be performed for each of these factors. Here                        is an example to help you understand this: If you have specified 500                        metres as the distance and 10 as the number of iterations (x-direction),                        the grid is moved horizontally in steps of 50 metres. The range for                        rotation iterations is between 0 and 90 (excluded) degrees for square                        based grids and 0 to 120 (excluded) degrees for triangle based grids.                       

Higher numbers of iterations do not necessarily lead to better                        results (it is even possible to get worse results). As a starting                        point, use the default values (5 iterations for each factor) and then                        experiment with different settings. Too many iterations can bring the                        computer to its limits and cause the plug-in (and QGIS itself) to                        crash. 10 iterations each should be feasible, beyond that it may get                        critical. If you run the plugin with a higher number of iterations,                        please leave QGIS alone to minimise the risk of crashes.</source>
        <translation>Dieser Algorithmus erwartet einen Polygonlayer und einen Wert &quot;Abstand zwischen den Punkten&quot;. Es wird versucht, unter Einhaltung der Abstandsbedingung eine Anordnung von Punkten zu finden, mit der eine eine möglichst große Anzahl von Punkten in dem Polygon untergebracht werden kann (beachten Sie hierzu den Vorbehalt im folgenden Absatz). Der Algorithmus gibt einen MultiPoint-Layer aus, der für jedes Merkmal des Eingabelayers ein Merkmal enthält. Seine Attribute sind ein Feld &quot;FID&quot; (int), das sich auf die FID des Eingabe-Features bezieht, und ein Feld &quot;NUMPOINTS&quot; (int), das die Anzahl der eingepassten Punkte angibt. Die Mehrpunktgeometrie enthält eine Anordnung von Punkten, die die höchste Punkteanzahl ergibt.\n\nBitte beachten Sie, dass es sich um einen Näherungsalgorithmus handelt, der darauf basiert, eine große Anzahl von möglichen Punktanordnungen zu testen. Bei diesem Ansatz kann nicht garantiert werden, tatsächlich die allerbeste Lösung gefunden wird.\n\nDie Berechnungsgrundlage für das Testverfahren sind regelmäßige Punktgitter. Sie können wählen, ob der Algorithmus quadratische Gitter, dreieckige Gitter oder beides verwenden soll. Bitte beachten Sie, dass quadratische Gitter nur in speziellen Fällen (relativ kleine, rechteckige Eingabepolygone) das optimale Ergebnis liefern.\n\nDer Algorithmus variiert die Gitter, indem er sie schrittweise in x- und y-Richtung verschiebt und dreht (und zwar alle Faktoren gleichzeitig). Sie können angeben, wie viele Iterationen für jeden dieser Faktoren durchgeführt werden sollen. Das folgende Beispiel soll dabei helfen, dies zu verstehen: Wenn Sie 500 Meter als Entfernung und 10 als Anzahl der Iterationen (x-Richtung) angegeben haben, wird das Gitter in Schritten von 50 Metern horizontal verschoben. Der Wertebereich für die Drehungen liegt zwischen 0 und 90 (ausgenommen) Grad bei quadratischen Gittern und zwischen 0 und 120 (ausgenommen) Grad bei dreieckigen Gittern.\n\nEine höhere Anzahl von Iterationen führt nicht unbedingt zu besseren Ergebnissen (es ist sogar möglich, schlechtere Ergebnisse zu erzielen). Verwenden Sie als Ausgangspunkt die Standardwerte (5 Iterationen für jeden Faktor) und experimentieren Sie dann mit verschiedenen Einstellungen. Zu viele Iterationen können den Computer an seine Grenzen bringen und das Plug-in (und QGIS selbst) zum Absturz bringen. Jeweils 10 Iterationen sollten machbar sein, darüber hinaus kann es kritisch werden. Wenn Sie das Plugin mit einer höheren Anzahl von Iterationen ausführen, dann lassen Sie QGIS bitte in Ruhe, um das Risiko von Abstürzen zu minimieren.</translation>
    </message>
</context>
<context>
    <name>PutSpacedPointsInPolygonsProvider</name>
    <message>
        <location filename="../pspip_provider.py" line="76"/>
        <source>User-created</source>
        <translation>Nutzerdefiniert</translation>
    </message>
</context>
</TS>
