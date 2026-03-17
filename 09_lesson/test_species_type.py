from add import SpeciesType, Session


def test_create_species_simple():
    session = Session()

    new_record = SpeciesType(type_id=8, type_name="овощи")
    session.add(new_record)
    session.commit()
    session.refresh(new_record)

    result = session.query(SpeciesType).filter(
        SpeciesType.type_id == 8).first()
    assert result is not None
    assert result.type_name == "овощи"

    session.delete(result)
    session.commit()
    session.close()


def test_update_species_name():
    session = Session()

    new_record = SpeciesType(type_id=10, type_name="фрукты")
    session.add(new_record)
    session.commit()
    session.refresh(new_record)

    result = session.query(SpeciesType).filter(
        SpeciesType.type_id == 10).first()
    assert result is not None
    assert result.type_name == "фрукты"

    result.type_name = "ягоды"
    session.commit()
    session.refresh(result)

    updated_record = session.query(SpeciesType).filter(
        SpeciesType.type_id == 10).first()
    assert updated_record is not None
    assert updated_record.type_name == "ягоды"

    session.delete(updated_record)
    session.commit()
    session.close()


def test_delete_species():
    session = Session()

    new_record = SpeciesType(type_id=12, type_name="грибы")
    session.add(new_record)
    session.commit()
    session.refresh(new_record)

    result = session.query(SpeciesType).filter(
        SpeciesType.type_id == 12
    ).first()
    assert result is not None

    session.delete(result)
    session.commit()

    deleted_record = session.query(SpeciesType).filter(
        SpeciesType.type_id == 12
    ).first()
    assert deleted_record is None
    session.close()
