import os
from PIL import Image
import sys

def compress_jpeg(file_path, quality=85):
    """压缩JPEG图片"""
    try:
        img = Image.open(file_path)
        # 保存原始图片的EXIF数据
        exif = img.info.get('exif')
        
        # 压缩图片
        img.save(file_path, 'JPEG', quality=quality, optimize=True, exif=exif)
        
        return True
    except Exception as e:
        print(f"压缩JPEG图片失败 {file_path}: {e}")
        return False

def compress_png(file_path):
    """压缩PNG图片"""
    try:
        img = Image.open(file_path)
        
        # 对于RGBA图片，转换为P模式（带透明度的调色板）
        if img.mode == 'RGBA':
            img.save(file_path, 'PNG', optimize=True, compress_level=9)
        else:
            img.save(file_path, 'PNG', optimize=True, compress_level=9)
        
        return True
    except Exception as e:
        print(f"压缩PNG图片失败 {file_path}: {e}")
        return False

def main():
    """主函数，遍历所有图片文件并压缩"""
    image_dir = 'image'  # 图片目录
    total_files = 0
    compressed_files = 0
    
    # 遍历所有文件和子目录
    for root, _, files in os.walk(image_dir):
        for file in files:
            file_path = os.path.join(root, file)
            file_ext = file.lower()
            
            # 检查是否为图片文件
            if file_ext.endswith('.jpg') or file_ext.endswith('.jpeg'):
                total_files += 1
                if compress_jpeg(file_path):
                    compressed_files += 1
            elif file_ext.endswith('.png'):
                total_files += 1
                if compress_png(file_path):
                    compressed_files += 1
    
    print(f"压缩完成！总共处理 {total_files} 个文件，成功压缩 {compressed_files} 个文件。")

if __name__ == "__main__":
    main()