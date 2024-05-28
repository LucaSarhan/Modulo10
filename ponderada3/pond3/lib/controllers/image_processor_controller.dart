import 'dart:convert';
import 'dart:io';
import 'package:http/http.dart' as http;
import 'package:image_picker/image_picker.dart';
import 'package:path_provider/path_provider.dart';
import 'package:path/path.dart' as path;
import 'package:flutter_dotenv/flutter_dotenv.dart';
import 'package:pond3/services/notification.dart';

class ImgProcessorController {
  final ImagePicker _picker = ImagePicker();

  Future<void> pickImage(String? username, String? email, Function setImage,
      Function setFilteredImage) async {
    final pickedFile = await _picker.pickImage(source: ImageSource.gallery);
    if (pickedFile != null) {
      setImage(File(pickedFile.path));
      setFilteredImage(null);

      final String? url = dotenv.env['URL'];
      final String? logger = dotenv.env['LOGGER'];
      await http.post(
        Uri.parse('$url/$logger/log'),
        body: jsonEncode({
          'username': username,
          'email': email,
          'action': 'image_picked',
          'datetime': DateTime.now().toIso8601String(),
        }),
        headers: {'Content-Type': 'application/json'},
      );
    }
  }

  Future<void> uploadImage(String? username, String? email, File? image,
      Function setLoading, Function setFilteredImage) async {
    if (image == null) return;

    setLoading(true);

    final String? url = dotenv.env['URL'];
    final String? imageFilter = dotenv.env['IMAGE_FILTER'];

    var request =
        http.MultipartRequest('POST', Uri.parse('$url/$imageFilter/upload'));
    request.files.add(await http.MultipartFile.fromPath('file', image.path));

    var response = await request.send();
    if (response.statusCode == 200) {
      var responseData = await response.stream.toBytes();
      var tempDir = await getTemporaryDirectory();
      var filePath = path.join(tempDir.path, 'filtered_image.jpg');
      File file = File(filePath);
      await file.writeAsBytes(responseData);
      setFilteredImage(file);
      setLoading(false);

      final String? logger = dotenv.env['LOGGER'];
      await http.post(
        Uri.parse('$url/$logger/log'),
        body: jsonEncode({
          'username': username,
          'email': email,
          'action': 'image_filtered',
          'datetime': DateTime.now().toIso8601String(),
        }),
        headers: {'Content-Type': 'application/json'},
      );

      NotificationService.showNotification('Image processed',
          'The image has been successfully processed. You can now download it.');
    } else {
      setLoading(false);
    }
  }
}
