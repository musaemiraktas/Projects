import 'package:flutter/material.dart';
import 'package:yazlab2_2/components/tile.dart';

class Grid extends StatelessWidget {
  final int crossAxisCount; // Sütun sayısı
  final int totalTiles;     // Toplam taş sayısı

  const Grid({
    super.key,
    required this.crossAxisCount, // Sütun sayısı için gereken parametre
    required this.totalTiles,     
  });


  @override
  Widget build(BuildContext context) {
    return GridView.builder(
      //physics: NeverScrollableScrollPhysics(),
      itemCount: totalTiles, 
      padding: EdgeInsets.fromLTRB(36, 45, 36, 20),
      gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
        mainAxisSpacing: 4,
        crossAxisSpacing: 4,
        crossAxisCount: crossAxisCount 
      ), 
      itemBuilder: (context, index){
        return Tile(index: index);
      }
    );
  }
}
