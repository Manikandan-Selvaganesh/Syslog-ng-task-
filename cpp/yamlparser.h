#ifndef YAMLPARSER_H
#define YAMLPARSER_H
#include <QObject>
#include "mainwindow.h"
class YamlParser : public QObject
{
Q_OBJECT
public:
explicit YamlParser(QObject *parent = 0);
void Init();
protected:
MainWindow* mainWindow;
private:
void LoadStyleSheet();
};
#endif // YAMLPARSER_H
