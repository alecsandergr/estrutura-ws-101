from pipeline import extract, transform, load

if __name__ == '__main__':
    listas_de_data_frame = extract.extract_from_excel('data/input')
    df = transform.concat_data_frames(listas_de_data_frame)
    msg = load.load_excel(df, 'data/output', 'consolidado')
    print(msg)