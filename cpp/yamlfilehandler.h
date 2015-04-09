#ifndef YAMLFILEHANDLER_H
#define YAMLFILEHANDLER_H
#include <QObject>
#include <QString>
#include <QDomDocument>
#include <QFile>
#include <QStringList>
#include <QTextStream>
class YamlFileHandler : public QObject
{
Q_OBJECT
public:
explicit YamlFileHandler(QString path,QObject *parent = 0);
void Init();
QDomDocument getYamlDocument();
QDomDocument yamlDocument;
private:
void ParseYamlFile();
QString yamlFilePath;
};
#endif // YAMLFILEHANDLER_H
