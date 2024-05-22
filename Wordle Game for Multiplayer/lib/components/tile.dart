import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:yazlab2_2/constants/answer_stages.dart';
import 'package:yazlab2_2/constants/colors.dart';
import 'package:yazlab2_2/providers/controller.dart';

class Tile extends StatefulWidget {
  const Tile({required this.index,
    super.key,
  });

  final int index;

  @override
  State<Tile> createState() => _TileState();
}

class _TileState extends State<Tile> {
  Color _backgroundcolor = Colors.transparent, _borderColor = lightThemeLightShade;
  late AnswerStage _answerStage;

  
  @override
  void initState() {
    WidgetsBinding.instance?.addPostFrameCallback((timeStamp) {
      _borderColor = Theme.of(context).primaryColorLight;
    });
    super.initState();
  }


  @override
  Widget build(BuildContext context) {
    return Consumer<Controller>(
      builder: (_, notifier, __){
        String text = "";
        Color fontColor = Colors.white;
        if(widget.index < notifier.tilesEntered.length){
          text = notifier.tilesEntered[widget.index].letter;
          _answerStage = notifier.tilesEntered[widget.index].answerStage;
          if(_answerStage == AnswerStage.correct){
            _backgroundcolor = correctGreen;
            _borderColor = Colors.transparent;
          }
          else if(_answerStage == AnswerStage.contains){
            _backgroundcolor = containsYellow;
            _borderColor = Colors.transparent;
          }
          else if(_answerStage == AnswerStage.incorrect){
            _backgroundcolor = Theme.of(context).primaryColorDark;
            _borderColor = Colors.transparent;
          }
          else{
            fontColor = Theme.of(context).textTheme.bodyText2?.color ?? Colors.black;
            _backgroundcolor = Colors.transparent;
            
          }


          return Container(
            decoration: BoxDecoration(
              color: _backgroundcolor,
              border: Border.all(
                color: _borderColor,
              )
            ),
            child: FittedBox(
              fit: BoxFit.contain,
              child: Padding(
                padding: const EdgeInsets.all(6.0),
                child: Text(text,
                style: TextStyle().copyWith(
                  color: fontColor
                ),
                ),
              )));
        }
        else{
          return Container(
            decoration: BoxDecoration(
              color: _backgroundcolor,
              border: Border.all(
                color: _borderColor,
              )
            ),
          );
        }
        
      });
  }
}