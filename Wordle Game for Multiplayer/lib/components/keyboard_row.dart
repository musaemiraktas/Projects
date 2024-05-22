import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:yazlab2_2/constants/answer_stages.dart';
import 'package:yazlab2_2/constants/colors.dart';
import 'package:yazlab2_2/providers/controller.dart';
import 'package:yazlab2_2/data/keys_map.dart';

class KeyboardRow extends StatelessWidget {
  const KeyboardRow({
    required this.min, 
    required this.max,
    super.key,
  });

  final int min, max;


  @override
  Widget build(BuildContext context) {
    final size = MediaQuery.of(context).size;
    return Consumer<Controller>(
      builder: (_, notifier, __) {
        int index = 0;
        return Row(
        mainAxisAlignment: MainAxisAlignment.center,
        children: keysMap.entries.map((e) {
          index++;
          if(index >= min && index <= max){
            Color color = Theme.of(context).primaryColorLight;
            Color keyColor = Colors.white;

            if(e.value == AnswerStage.correct){
              color = correctGreen;
            }
            else if(e.value == AnswerStage.contains){
              color = containsYellow;
            }
            else if(e.value == AnswerStage.incorrect){
              color = Theme.of(context).primaryColorDark;
            }
            else{
              keyColor = Theme.of(context).textTheme.bodyText2?.color ?? Colors.black;
            }

            return Padding(
              padding: EdgeInsets.all(size.width * 0.005),
              child: ClipRRect(
                borderRadius: BorderRadius.circular(7),
                child: SizedBox(
                  width: e.key == 'ENTER' || e.key == 'SİL' ? 
                  size.width * 0.13 :
                  size.width * 0.07,
                  height: size.height * 0.090,
                  child: Material(
                    color: color,
                    child: InkWell(
                      onTap: (){
                        Provider.of<Controller>(context, listen: false).setKeyTapped(value: e.key);
                      },
                      child: Center(child: 
                      e.key == 'SİL' ? const Icon(Icons.backspace_outlined) :
                      Text(e.key,
                      style: Theme.of(context).textTheme.bodyText2?.copyWith(
                        color: keyColor,
                      ),
                      ))),
                  )),
              ),
            );
          }
          else{
            return const SizedBox();
          }
        }).toList(),
      );
      },
    );
  }
}